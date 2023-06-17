#pragma once

#include <iostream>
#include <cstdlib>
#include <string>
#include <windows.h>
#include <fstream>

extern "C" __declspec(dllexport) bool AddUserInDB(char name[], char surname[], char idnumber[], char password[]);
extern "C" __declspec(dllexport) bool SearchUserInDB(char name[], char surname[], char idnumber[], char password[]);
extern "C" __declspec(dllexport) bool AddDeclaration(char name[], char surname[], char idnumber[], char housadress[], char service[], int cost);
extern "C" __declspec(dllexport) void RemoveDeclaration(char name[], char surname[], char idnumber[]);
extern "C" __declspec(dllexport) bool SeekDeclarationInDB(char name[], char surname[], char idnumber[], char service[]);