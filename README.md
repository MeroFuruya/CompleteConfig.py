# CompleteConfig.py

This is a Python Module to read and write CompleteConfig files. This format is from a Kotlin/FabricMC project called [CompleteConfig](https://github.com/Lortseam/completeconfig).

## Usage

The module has a feel like the JSON module.
To read a file, just do:

```python
with open("file.config", "r") as f:
    config = completeconfig.load(f)
```

To write a file, just do:

```python
with open("file.config", "w") as f:
    completeconfig.dump(config, f)
```

## Comments

The key of a commented line is represented with the `Key` object. It has a `comment` attribute that contains the comment.

It can accesed via `Key("KeyName")` or `"keyName"`.

## String-Keys

The key of a string-keyed map is represented with the `StrKey` object. It has a `value` attribute that contains the key.
the key can also be accesed by converting the `StrKey` object to a string.

It can accesed via `StrKey("KeyName")` or `"keyName"`.
