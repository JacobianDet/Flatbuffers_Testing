#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include "client_generated.h"

using namespace CrossParser;

int main(int argc, char **argv) {
    if (argc < 2) {
        std::cerr << "Format: ./fb_decoder <path-to-fb_bytes.bin>\n";
        return 1;
    }

    std::string file_path(argv[1]);
    file_path += "fb_bytes.bin";
    std::ifstream infile(file_path, std::ios::in | std::ios::binary);
    if (!infile.is_open()) {
        std::cerr << "Issue with file opening, please check\n";
        return 2;
    }

    infile.seekg(0, std::ios::end);
    int size = infile.tellg();
    infile.seekg(0, std::ios::beg);
    char *buf = new char[size];
    infile.read(buf, size);
    infile.close();

    auto root_client_vector = GetClientVec(buf);
    auto clients_vector = root_client_vector->client_vec();
    for (unsigned int i=0; i<clients_vector->size(); ++i) {
        switch (clients_vector->get(i)->client_elem_type()) {
            case ClientUnion_Person: {
                auto person = clients_vector->get(i)->client_elem();
                std::cout << "Data of type Person. Output:\n";
                std::cout << "{" << person->name()->c_str() << " ,"
                          << person->age() << " ," << person->weight()
                          << " ," << person->gender()->c_str()
                          << "}\n";
                break;
            }
            
            case ClientUnion_Group: {
                auto group = clients_vector->get(i)->client_elem();
                std::cout << "Data of type Group. Output:\n";
                std::cout << "{" << group->group_name()->c_str()
                          << " ," << group->avg_age() << " ,"
                          << group->avg_weight() << " ,{";
                auto client_group_vec_names = group->person_names();
                for (unsigned int j=0; j<client_group_vec_names->size(); ++j) {
                    std::cout << client_group_vec_names->get(j)->c_str() << " ,";
                }
                std::cout << "}}\n";
                break;
            }
        }
    }

    delete [] buf;
    return 0;
}
