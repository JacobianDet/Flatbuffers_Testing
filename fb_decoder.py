import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'flatbuffers/python/'))

import flatbuffers

import CrossParser.Person
import CrossParser.Group
import CrossParser.ClientUnion 
import CrossParser.Client
import CrossParser.ClientVec

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Format: fb_decoder.py <path-to-fb_bytes.bin>", file=sys.stderr)
        exit(1)

    file_path = sys.argv[1]
    file_path += "fb_bytes.bin"

    with open(file_path, "rb") as infile:

        buf = infile.read()
        buf = bytearray(buf)
        root_client_vec = CrossParser.ClientVec.ClientVec.GetRootAsClientVec(buf, 0)
        for i in range(root_client_vec.ClientVecLength()):
            union_type = root_client_vec.ClientVec(i).ClientElemType()
            union_elem = root_client_vec.ClientVec(i).ClientElem()
            if union_type == CrossParser.ClientUnion.ClientUnion().Person:
                person = CrossParser.Person.Person()
                person.Init(union_elem.Bytes, union_elem.Pos)
                print("Data of type Person. Output:")
                print(f"{{{person.Name().decode()}, {person.Age()}, {person.Weight()}, {person.Gender().decode()}}}")

            elif union_type == CrossParser.ClientUnion.ClientUnion().Group:
                group = CrossParser.Group.Group()
                group.Init(union_elem.Bytes, union_elem.Pos) 
                print("Data of type Group. Output:")
                print(f"{{{group.GroupName().decode()}, {group.AvgAge()}, {group.AvgWeight()}, {{", end="")
                for j in range(group.PersonNamesLength()):
                    if j:
                        print(", ", end="")
                    print(f"{group.PersonNames(j).decode()}", end="")
                print("}}") 
