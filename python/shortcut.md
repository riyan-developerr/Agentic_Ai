Here are the Windows shortcuts that save the most time, grouped by what you're doing. Start with the "learn these first" list at the bottom.

## Move around fast

| Shortcut | What it does |
|---|---|
| `Ctrl + P` | Open any file by typing part of its name |
| `Ctrl + Shift + P` | Command Palette (search any VS Code command) |
| `Ctrl + G` | Go to a line number |
| `Ctrl + Shift + O` | Jump to a function/class in the current file |
| `F12` | Go to where something is defined |
| `Shift + F12` | Show everywhere something is used |
| `Alt + ←` / `Alt + →` | Go back / forward to where you were |
| `Ctrl + Tab` | Switch between open files |
| `Ctrl + B` | Show/hide the sidebar |
| `` Ctrl + ` `` | Show/hide the terminal |
| `Ctrl + \` | Split the editor into two panes |

## Edit faster

| Shortcut | What it does |
|---|---|
| `Alt + ↑` / `Alt + ↓` | Move the current line up/down |
| `Shift + Alt + ↑` / `↓` | Copy the current line up/down |
| `Ctrl + Shift + K` | Delete the whole line |
| `Ctrl + /` | Comment/uncomment the line |
| `Ctrl + Enter` | New line below (cursor can be anywhere on the line) |
| `Ctrl + Shift + Enter` | New line above |
| `Ctrl + D` | Select the next match of the selected word |
| `Ctrl + Shift + L` | Select all matches of the selected word |
| `Alt + Click` | Add another cursor where you click |
| `F2` | Rename a variable/function everywhere |
| `Ctrl + .` | Quick fix / suggestions for an error |
| `Shift + Alt + F` | Auto-format the file |
| `Ctrl + Backspace` | Delete the previous word |

## Search and replace

| Shortcut | What it does |
|---|---|
| `Ctrl + F` | Find in the current file |
| `Ctrl + H` | Find and replace in the current file |
| `Ctrl + Shift + F` | Search across the whole project |
| `Ctrl + Shift + H` | Replace across the whole project |

## Run and debug

| Shortcut | What it does |
|---|---|
| `F5` | Start debugging |
| `Ctrl + F5` | Run without debugging |
| `F9` | Add/remove a breakpoint |
| `F10` / `F11` | Step over / step into |

## Example: three shortcuts working together

Say you have this Python code:

```python
def add(a, b):
    return a + b

total = add(1, 2)
print(add(3, 4))
```

1. Click on `add` and press `F2`, type `sum_two`, press Enter. It renames the function in all three places at once.
2. Select `total`, press `Ctrl + D` to select the next `total`, and edit both at the same time.
3. Put your cursor on the `print` line and press `Shift + Alt + ↓` to duplicate it, then change the numbers.

## Learn these 8 first

`Ctrl + P`, `Ctrl + Shift + P`, `Alt + ↑/↓`, `Ctrl + D`, `F2`, `Ctrl + /`, `` Ctrl + ` ``, `Ctrl + Shift + F`

Once those feel automatic, add the rest. To see or change any shortcut, press `Ctrl + K` then `Ctrl + S`.