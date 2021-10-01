# sizer

Sizer is a simple utility for generating information about a SlotC project's art. 
The information gathered will be color format, image size, frame size, and the number of frames.
Additionally a png will be created for each .img in the rc folder.

## Installation

```bash
git clone repo
```

## Usage

Place size.py into the root directory of a SlotC project or copy your rc folder from an SlotC project into the src folder of sizer and run 

```python
python3 size.py  
```

The format of the generated information is as follows  

```txt
image_1.img
Format: RGBA
Colorkey: No
Image size: 165x270
Frame size: 165x90
Frames: 3

image_2.img
Format: RGBA
Colorkey: No
Image size: 165x270
Frame size: 165x90
Frames: 3
```

## Contributing

Changes are welcome please make a pull request and make sure your changes pass all of the test cases. 

## Author

Nicholas.Janulewicz@gmail.com 

## License
[MIT](https://choosealicense.com/licenses/mit/)