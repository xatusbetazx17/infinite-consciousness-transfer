# Example Scan Data

This directory contains sample brain scan files for testing and demonstration purposes. These scans can be used by the `NeuralMapper` to generate computational models and by the simulation pipeline to produce visualizations.

## File Formats

* **NIfTI (.nii, .nii.gz)**: Standard neuroimaging format. Contains volumetric data representing MRI scans.
* **Raw Binary (.bin)**: Custom binary dumps of float32 voxel data (for advanced testing).

## Example Files

| Filename                      | Description                                             |
| ----------------------------- | ------------------------------------------------------- |
| `sample_mri.nii.gz`           | Compressed NIfTI file with a 64×64×64 volume.           |
| `phantom_scan.nii`            | Uncompressed NIfTI representing a spherical phantom.    |
| `synthetic_data_shape_32.bin` | Raw binary float32 data for 32×32×32 synthetic volumes. |

## Usage

1. **Default Scan**
   The simulation environment will load `sample_mri.nii.gz` if no `scan_path` is provided:

   ```python
   graph = neural_mapper.map_scan(
       scan_path="data/example_scan/sample_mri.nii.gz",
       config={ 'threshold': 0.1, 'max_edges': 50000 }
   )
   ```

2. **Replacing or Extending**

   * To add your own scans, place `.nii`, `.nii.gz`, or `.bin` files here.
   * Ensure filenames match the patterns expected by your configuration or scripts.

3. **Custom Configurations**
   For raw binary files, specify the `shape` in your config:

   ```python
   graph = neural_mapper.map_scan(
       scan_path="data/example_scan/synthetic_data_shape_32.bin",
       config={ 'shape': (32,32,32), 'threshold': 0.05, 'max_edges': 10000 }
   )
   ```

---

*Note: The sample NIfTI files provided here are for demonstration only. For real data, acquire scans through appropriate neuroimaging pipelines.*
