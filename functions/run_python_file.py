import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(full_path)
    if not abs_target.startswith(abs_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    if not abs_target.endswith(".py"):
        return f'Error:"{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ["python", abs_target] + args,
            timeout=30,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        return f"Process exited with code {e.returncode}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    if result.returncode is None:
        return "No output produced"
    return f"STDOUT:{result.stdout} \nSTDERR:{result.stderr}"
