// dllmain.cpp : Defines the entry point for the DLL application.
#include <windows.h>
#include <cstdio>
#include <iostream>

void DllThread() 
{
    Beep(500, 800);
    AllocConsole();
    FILE* f;
    freopen_s(&f, "CONOUT$", "w", stdout);
    std::cout << "Cheat Injected" << std::endl;
}

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        CloseHandle(CreateThread(0, 0, (LPTHREAD_START_ROUTINE)DllThread, hModule, 0, 0));
        break;
    }
    return TRUE;
}

