#include "Header.h"

extern "C" __declspec(dllexport) bool AddUserInDB(char name[], char surname[], char idnumber[], char password[])
{
    std::string folderPath = "D:\\Project\\database\\";
    std::string UserFolder = (std::string)name + (std::string)surname + (std::string)idnumber;
    //Перевірка чи існує папка з файлом
    DWORD fileAttributes = GetFileAttributesA((folderPath + UserFolder).c_str());
    if (fileAttributes != INVALID_FILE_ATTRIBUTES && (fileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
        std::fstream User_Info(folderPath + UserFolder + "\\user.txt");
        if (User_Info.is_open()) {
            User_Info.close();
            return false;
        }
    }
    //Створюємо папку з інформацією про користувача
    std::system(("mkdir " + folderPath + UserFolder).c_str());
    std::fstream User_Info(folderPath + UserFolder + "\\user.txt", std::ios::out);
    User_Info << name << " " << surname << " " << idnumber << " " << password;
    User_Info.close();
    return true;
}

extern "C" __declspec(dllexport) bool SearchUserInDB(char name[], char surname[], char idnumber[], char password[]) {
    std::string folderPath = "D:\\Project\\database\\";
    std::string UserFolder = (std::string)name + (std::string)surname + (std::string)idnumber;

    //Перевірка чи існує папка з файлом
    DWORD fileAttributes = GetFileAttributesA((folderPath + UserFolder).c_str());
    if (fileAttributes != INVALID_FILE_ATTRIBUTES && (fileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
        std::fstream User_Info(folderPath + UserFolder + "\\user.txt", std::ios::in);
        // Перевірка чи збігаються дані
        if (User_Info.is_open()) {
            std::string user_name, user_surname, user_id, user_password;
            User_Info >> user_name >> user_surname >> user_id >> user_password;
            if (!strcmp(name, user_name.c_str()) && !strcmp(surname, user_surname.c_str())
            && !strcmp(idnumber, user_id.c_str()) && !strcmp(password, user_password.c_str())) {
                return true;
            }
        }
    }
    return false;

}

extern "C" __declspec(dllexport) bool AddDeclaration(char name[], char surname[], char idnumber[], char housadress [], char service[], int cost) {
    std::string folderPath = "D:\\Project\\database\\";
    std::string UserFolder = (std::string)name + (std::string)surname + (std::string)idnumber;

    //Перевірка чи існує файл
    std::fstream Declar(folderPath + UserFolder + "\\" + (std::string)service + ".txt", std::ios::in);
    if (Declar.is_open()) {
        Declar.close();
        return false;
    }
    //Додаємо послугу для сплати
    Declar.open(folderPath + UserFolder + "\\" + (std::string)service + ".txt", std::ios::out);
    Declar << housadress << std::endl;
    Declar << service << " " << cost;
    return true;
}

extern "C" __declspec(dllexport) void RemoveDeclaration(char name[], char surname[], char idnumber[]) {
    std::string folderPath = "D:\\Project\\database\\";
    std::string UserFolder = (std::string)name + (std::string)surname + (std::string)idnumber;

    const char* services[] = { "water", "trash", "gas", "light" };
    int n = sizeof(services) / sizeof(char*);

    for (int i = 0; i < n; i++) {
        std::fstream Declar(folderPath + UserFolder + "\\" + (std::string)services[i] + ".txt", std::ios::in);
        if (Declar.is_open()) {
            Declar.close();
            remove((folderPath + UserFolder + "\\" + (std::string)services[i] + ".txt").c_str());
        }
    }
}

extern "C" __declspec(dllexport) bool SeekDeclarationInDB(char name[], char surname[], char idnumber[], char service[]) {
    std::string folderPath = "D:\\Project\\database\\";
    std::string UserFolder = (std::string)name + (std::string)surname + (std::string)idnumber;

    std::fstream Declar(folderPath + UserFolder + "\\" + (std::string)service + ".txt", std::ios::in);
    if (Declar.is_open()) {
        Declar.close();
        return false;
    }

    return true;
}

extern "C" __declspec(dllexport) int CountSummDeclaration(char name[], char surname[], char idnumber[]) {
    std::string folderPath = "D:\\Project\\database\\";
    std::string UserFolder = (std::string)name + (std::string)surname + (std::string)idnumber;

    int sum = 0;

    const char* services[] = { "water", "trash", "gas", "light" };
    int n = sizeof(services) / sizeof(char*);

    std::string addres, service;
    int price;

    for (int i = 0; i < n; i++) {
        std::fstream Declar(folderPath + UserFolder + "\\" + (std::string)services[i] + ".txt", std::ios::in);
        if (Declar.is_open()) {
            std::getline(Declar, addres);
            Declar >> service >> price;
            sum += price;
        }
    }

    return sum;
}