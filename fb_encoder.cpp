#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "client_generated.h"

using namespace CrossParser;

int main(int argc, char **argv) {
    if (argc < 2) {
        std::cerr << "Format: ./fb_encoder <path-to-fb_bytes.bin>\n";
        return 1;
    }

    std::string file_path(argv[1]);
    file_path += "fb_bytes.bin";
    std::ofstream outfile(file_path, std::ios::out | std::ios::binary);
    if (!outfile.is_open()) {
        std::cerr << "Issue with file opening, please check\n";
        return 2;
    }

    flatbuffers::FlatBufferBuilder builder;
    
    auto client_person_name = builder.CreateString("Ram");
    double client_person_age = 21;
    double client_person_weight = 76.5;
    auto client_person_gender = builder.CreateString("Male");

    auto client_group_name = builder.CreateString("FightClub");
    double client_group_avg_age = 24.5;
    double client_group_avg_weight = 66;
    std::vector<std::string> tmp_vec_names{"Ram", "Shyam", "Raghuveer"};
    auto client_group_vec_names = builder.CreateVectorOfStrings(tmp_vec_names);

    auto person = CreatePerson(builder, client_person_name, client_person_age, client_person_weight, client_person_gender);
    auto group = CreateGroup(builder, client_group_name, client_group_avg_age, client_group_avg_weight, client_group_vec_names);

    auto client_person = CreateClient(builder, ClientUnion_Person, person.Union());
    auto client_group = CreateClient(builder, ClientUnion_Group, group.Union());

    std::vector<flatbuffers::Offset<Client>> tmp_vec_clients{client_person, client_group};
    auto clients_vector = builder.CreateVector(tmp_vec_clients);
    auto root_client_vector = CreateClientVec(builder, clients_vector);

    builder.Finish(root_client_vector);
    uint8_t *buf = builder.GetBufferPointer();
    int size = builder.GetSize();
    outfile.write(reinterpret_cast<const char*>(buf), size);
    outfile.close();
    return 0;
}
