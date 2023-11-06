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
        print("Format: fb_encoder.py <path-to-fb_bytes.bin>", file=sys.stderr)
        exit(1)

    file_path = sys.argv[1]
    file_path += "fb_bytes.bin"

    with open(file_path, "wb") as outfile:

        builder = flatbuffers.Builder(0)

        client_person_name = builder.CreateString("Ram")
        client_person_gender = builder.CreateString("Male")
        CrossParser.Person.Start(builder)
        CrossParser.Person.AddName(builder, client_person_name)
        CrossParser.Person.AddAge(builder, 21)
        CrossParser.Person.AddWeight(builder, 76.5)
        CrossParser.Person.AddGender(builder, client_person_gender)
        person = CrossParser.Person.End(builder)

        client_group_name = builder.CreateString("FightClub")
        string_offset_list = []
        string_offset_list.append(builder.CreateString("Raghuveer"))
        string_offset_list.append(builder.CreateString("Shyam"))
        string_offset_list.append(builder.CreateString("Ram"))
        CrossParser.Group.StartPersonNamesVector(builder, 3)
        for string_offset in string_offset_list:
            builder.PrependUOffsetTRelative(string_offset)
        client_group_vec_names = builder.EndVector() 
        CrossParser.Group.Start(builder)
        CrossParser.Group.AddGroupName(builder, client_group_name)
        CrossParser.Group.AddAvgAge(builder, 24.5)
        CrossParser.Group.AddAvgWeight(builder, 66)
        CrossParser.Group.AddPersonNames(builder, client_group_vec_names)
        group = CrossParser.Group.End(builder)

        CrossParser.Client.Start(builder)
        CrossParser.Client.AddClientElemType(builder, CrossParser.ClientUnion.ClientUnion().Person)
        CrossParser.Client.AddClientElem(builder, person)
        client_person = CrossParser.Client.End(builder)

        CrossParser.Client.Start(builder)
        CrossParser.Client.AddClientElemType(builder, CrossParser.ClientUnion.ClientUnion().Group) 
        CrossParser.Client.AddClientElem(builder, group)
        client_group = CrossParser.Client.End(builder)

        CrossParser.ClientVec.StartClientVecVector(builder, 2)
        for offset_val in [client_group, client_person]:
            builder.PrependUOffsetTRelative(offset_val)
        clients_vector = builder.EndVector()
        CrossParser.ClientVec.Start(builder)
        CrossParser.ClientVec.AddClientVec(builder, clients_vector)
        root_client_vector = CrossParser.ClientVec.End(builder)

        builder.Finish(root_client_vector)
        buf = builder.Output()
        outfile.write(buf)
