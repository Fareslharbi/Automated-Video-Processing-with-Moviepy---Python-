# Automated Video Processing with Moviepy - Python

This project provides a collection of Python scripts that automate video processing tasks using the Moviepy library. Moviepy is a versatile library for video editing and manipulation.

## Features

- **1_vid_to_img.py**: Converts a video file into a sequence of images.
- **2_img_to_vid.py**: Converts a sequence of images into a video file.
- **3_create_gif.py**: Creates a GIF animation from a sequence of images.
- **4_audio_mix.py**: Mixes audio files with a video file.
- **5_overlay_text.py**: Adds text overlays to a video.

## Prerequisites

Before running the project, make sure you have the following requirements installed:

- Python (version 3.x)
- Moviepy library

You can install the required libraries by running the following command:

```
pip install moviepy
```

## Usage

1. Clone this repository or download the project files to your local machine.

2. Place your input files in the `data/samples/inputs` directory.

3. Open the desired script (e.g., `1_vid_to_img.py`) in a text editor and set the necessary parameters such as input file paths, output file paths, and any additional options specific to the script.

4. Run the script using the command:

   ```
   python 1_vid_to_img.py
   ```

   Replace `1_vid_to_img.py` with the name of the script you want to run.

5. The script will process the input files and generate the corresponding output files in the `data/samples/outputs` directory.

6. Repeat steps 3-5 for other scripts as needed.

## Configuration

The `conf.py` file provides configuration variables for the project. You can modify the `BASE_DIR`, `DATA_DIR`, `SAMPLE_DIR`, `SAMPLE_INPUTS`, and `SAMPLE_OUTPUTS` variables to customize the file paths and directories used by the scripts.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to the terms of the license.

## Disclaimer

Please use this project responsibly and ensure compliance with any applicable laws and regulations regarding video processing and content usage rights.
