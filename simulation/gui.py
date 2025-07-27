"""
3D Visualization GUI for Infinite Consciousness Transfer Framework

Integrates Blender-based rendering with core modules:
- NeuralMapper for scan-to-graph
- EmulationManager for consciousness simulation
- PhysicsEngine for programmable reality
- IdentityManager for snapshotting
- NewMath and EthicsFirewall for logic and compliance
"""
import bpy
import math
import random
from time import sleep
from utilities.newmath import NewMath
from neural_mapper import neural_mapper
from emulation_runtime import emulation_manager
from physics_engine import physics_engine
from identity_manager import identity_manager
from advanced_modules.ethics_firewall import EthicsFirewall

# Initialize utilities
nm = NewMath()
ethics = EthicsFirewall()

# Define neuron types with RGBA colors
neuron_types = {
    "Pyramidal":        (1, 0.2, 0.2, 1),
    "Interneuron":      (0.2, 0.8, 0.2, 1),
    "MirrorNeuron":     (0.2, 0.6, 1,   1),
    "DreamWeaver":      (0.8, 0.5, 1,   1),
    "Hyperintuition":   (1.0, 1.0, 0.2, 1),
    "TemporalAnchor":   (0.2, 1.0, 0.8, 1),
    "MetaCognition":    (1.0, 0.4, 0.0, 1),
    "InfinityNode":     (1,   1,   1,   1)
}

# Store created neuron objects\ nneuron_objects = []

def clear_scene():
    """Remove all objects, meshes, materials, and curves from the Blender scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for mesh in list(bpy.data.meshes): bpy.data.meshes.remove(mesh)
    for mat in list(bpy.data.materials): bpy.data.materials.remove(mat)
    for curve in list(bpy.data.curves): bpy.data.curves.remove(curve)


def create_neuron(name, location, color):
    """Add an icosphere neuron at location with emissive material color."""
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=0.1, location=location)
    neuron = bpy.context.active_object
    neuron.name = name
    mat = bpy.data.materials.new(name=f"Mat_{name}")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    emission = nodes.new('ShaderNodeEmission')
    emission.inputs[0].default_value = color
    emission.inputs[1].default_value = 3.0 + random.random() * 2
    output = nodes.get('Material Output')
    links.new(emission.outputs[0], output.inputs[0])
    neuron.data.materials.append(mat)
    return neuron


def add_pulse_animation(obj, start_frame=1, duration=40):
    """Animate object scale to simulate neuron firing pulse."""
    obj.scale = (1, 1, 1)
    obj.keyframe_insert(data_path='scale', frame=start_frame)
    peak = nm.exponentiate(1.3, 2)  # ~1.69
    obj.scale = (peak, peak, peak)
    obj.keyframe_insert(data_path='scale', frame=start_frame + duration//2)
    obj.scale = (1, 1, 1)
    obj.keyframe_insert(data_path='scale', frame=start_frame + duration)


def generate_reactive_neurons(count=200):
    """Create neurons with random types and pulse animations."""
    global neuron_objects
    for i in range(count):
        label = random.choice(list(neuron_types.keys()))
        loc = (random.uniform(-2,2), random.uniform(-2,2), random.uniform(-2,2))
        n = create_neuron(label, loc, neuron_types[label])
        neuron_objects.append(n)
        if i % 20 == 0:
            add_pulse_animation(n, start_frame=10 + i*2, duration=30)


def create_dynamic_synapses(count=100):
    """Add glowing curve paths to represent synaptic connections."""
    for _ in range(count):
        bpy.ops.curve.primitive_nurbs_path_add(location=(
            random.uniform(-3,3), random.uniform(-3,3), random.uniform(-3,3)))
        path = bpy.context.active_object
        path.scale = (random.uniform(0.1,0.3),) * 3
        mat = bpy.data.materials.new(name='SynapseMat')
        mat.use_nodes = True
        nodes = mat.node_tree.nodes; links = mat.node_tree.links
        # Clear and setup emission
        for node in list(nodes): nodes.remove(node)
        em = nodes.new('ShaderNodeEmission')
        em.inputs[0].default_value = (0.9,0.3,1,1)
        em.inputs[1].default_value = 4.0
        out = nodes.new('ShaderNodeOutputMaterial')
        links.new(em.outputs[0], out.inputs[0])
        path.data.materials.append(mat)


def create_label(text, location, size=0.4):
    """Add 3D text label at specified location."""
    bpy.ops.object.text_add(location=location)
    label = bpy.context.active_object
    label.data.body = text
    label.data.size = size
    label.rotation_euler = (math.radians(90), 0, 0)
    return label


def build_animated_brain_field(scan_path=None, scan_config=None, ticks=5):
    """
    Full pipeline: map scan → simulate consciousness → snapshot → render scene.
    """
    # 1. Prepare simulation graph
    cfg = scan_config or {'shape': (16,16,16), 'threshold': 0.1, 'max_edges': 2000}
    graph = neural_mapper.map_scan(scan_path, cfg)
    # 2. Run simulation ticks
    emu = emulation_manager
    emu.load_graph(graph)
    context = emu.run(steps=ticks)
    # 3. Apply physics
    context = physics_engine.apply(context)
    # 4. Snapshot
    identity_manager.create_snapshot(context, metadata={'render': True})
    # 5. Render in Blender
    clear_scene()
    generate_reactive_neurons(count=150)
    create_dynamic_synapses(count=80)
    create_label("∞ Consciousness Active", (2,0,-1), size=0.5)
    create_label("🧮 Logic Matrix", (2,0,-0.5), size=0.4)
    create_label("🎭 Emotional Field", (2,0,0), size=0.4)
    # 6. Play animation
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = ticks * 20


if __name__ == "__main__":
    # Example usage: run with default parameters
    build_animated_brain_field()
    print("3D brain field visualization built. Preview in Blender timeline.")
