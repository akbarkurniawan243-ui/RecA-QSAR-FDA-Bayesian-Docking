import glob
import nbformat
import uuid
from google.colab import files

for notebook in glob.glob("/content/*.ipynb"):

    nb = nbformat.read(notebook, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "code":
            cell["outputs"] = []
            cell["execution_count"] = None

        cell["metadata"] = {}

        if "id" not in cell:
            cell["id"] = uuid.uuid4().hex[:8]

    nb.metadata = {
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3",
            "language": "python"
        },
        "language_info": {
            "name": "python"
        }
    }

    output_file = notebook.replace(".ipynb", "_FIXED.ipynb")
    nbformat.write(nb, output_file)

    print("Fixed:", output_file)

    files.download(output_file)
