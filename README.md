# dfmt-sublime

Integration of [**dfmt**](https://github.com/Hackerpilot/dfmt) with Sublime Text.

**Note 1:** You need `dfmt` placed in your PATH.

**Note 2:** I use Sublime Text 2, therefore I can't test it with ST 3. And only Windows...

**Note 3:** I have no experience with Python before.


## Installation


### Method 1

#### Sublime Text 2

Place `dformat.sublime-package` file into your `Installed Packages` directory and restart Sublime to install the package.

#### Sublime Text 3

Place `dformat.sublime-package` file into your `<Sublime Text 3>\Packages` directory.

### Method 2

Copy `dformat.py` to your packages directory (`Preferences` -> `Browse Packages`)

Add shortcut (`Preferences` -> `Key Bindings - User`)

```
{
    { "keys": ["ctrl+alt+f"], "command": "dformat" }
}
```

You can add an option to the context menu (file: `Context.sublime-menu`)

```
[  
    { "command": "dformat", "caption": "DFormat" }  
] 
```

Or/and you can add an option to the main menu (file: `Main.sublime-menu`)

```
[
{  
    "caption":"DLang",
    "id": "dlang",
    "children":  
    [  
        {
            "caption": "DFormat", "command": "dformat"
        }
    ]  
}  
]
```
