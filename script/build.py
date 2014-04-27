import os
import re
import subprocess
import sys


words = [
    'source_files',
    'license',
    'source',
    'requires_arc'
]
file_contents = {}


def get_lines(filename):
    if filename in file_contents:
        return file_contents[filename]
    with open(filename, "r") as f:
        lines = f.readlines()
        file_contents[filename] = lines
        return lines


def command_success(command):
    with open(os.devnull, "w") as f:
        return subprocess.call(command.split(),
                               stderr=f,
                               stdout=f) == 0


def spec_identifier(filename):
    contents = get_lines(filename)
    for line in contents:
        if "Pod::Spec.new" in line:
            create_line = line
            break
    return re.findall(r"\|\w+\|", create_line)[0].strip("|")


def run_command(command):
    out = subprocess.Popen(command.split(),
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    return out.stdout.readlines()


def line_of_attr(attr, fname):
    identifier = spec_identifier(fname)
    contents = get_lines(fname)
    for idx, line in enumerate(contents):
        string = "%s.%s" % (identifier, attr)
        if line.strip().startswith(string):
            return idx + 1
    return idx - 1


def main(filename):
    if not command_success("pod --version"):
        print "Pod command missing or broken"
        return

    output = run_command("pod spec lint " + filename)
    output = output[2:]
    output = output[:-3]
    cleaned = []
    for line in output:
        l = line.strip(' -\n\t')
        if l:
            cleaned.append(l)

    errs = []
    for err in cleaned:
        for w in words:
            if w in err:
                ln = line_of_attr(w, filename)
                errs.append((ln, err))
                break

    for ln, err in errs:
        print "%s:%d:%s" % (filename, ln, err)


if __name__ == '__main__':
    main(sys.argv[1])
