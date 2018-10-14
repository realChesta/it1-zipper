# Informatics 1 zipper

This is a script that creates zip-files from finished exercises in IT1.

## Installation

1. Download the script using git:

   ```shell
   $ git clone https://github.com/realChesta/it1-zipper.git
   ```

2. Move `zipper.py` to the directory containing your exercise folders. <br/> *(or use the `-d` argument, see further below)*

3. Create a file named `config.json` in that same directory. It should look like this:

   ```json
   {
       "name": "hans",
       "surname": "muster",
       "student-id": 12345678
   }
   ```
   Obviously, you have to replace the data with your own name and id.
   
   You can also use the `-c` argument and place the config file in a different folder.


## Usage

Here's an example on how to zip exercises 3 and 4:
```shell
$ python zipper.py 4 5
```

### Arguments

* `-c --config [path]` sets a custom path to the config file. Default is `"config.json"`.
* `-d --directory [path]` set a custom exercises directory. Useful if script is not in the same directory. Default is the script's directory.