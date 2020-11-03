# Standard Library
import os

OS_SUCCESS_CODE = 0

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)

temp_dot_file = current_dir + "/db.dot"
output_path = base_dir + "/docs/img/updated-database-graph.svg"

cmd = (
    f"python {base_dir}/manage.py graph_models -a > {temp_dot_file}  && "
    f"dot -Tsvg {temp_dot_file} -o {output_path} && "
    f"rm {temp_dot_file}"
)

print("Generating database graph...")

if os.system(cmd) == OS_SUCCESS_CODE:
    print("Done!")
    print(f"Saved at: {output_path}")
else:
    print("Graph couldn't generate.")
    exit(1)

exit(0)
