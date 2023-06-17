import ctypes
DataBaseDLL = ctypes.CDLL("./DataBase.dll")

AddUserInDB = DataBaseDLL.AddUserInDB
AddUserInDB.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
AddUserInDB.restype = ctypes.c_bool

SearchUserInDB = DataBaseDLL.SearchUserInDB
SearchUserInDB.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
SearchUserInDB.restype = ctypes.c_bool

AddDeclaration = DataBaseDLL.AddDeclaration
AddDeclaration.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
AddDeclaration.restype = ctypes.c_bool

SeekDeclarationInDB = DataBaseDLL.SeekDeclarationInDB
SeekDeclarationInDB.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
SeekDeclarationInDB.restype = ctypes.c_bool

RemoveDeclaration = DataBaseDLL.RemoveDeclaration
RemoveDeclaration.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]

CountSummDeclaration = DataBaseDLL.CountSummDeclaration
CountSummDeclaration.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
CountSummDeclaration.restype = ctypes.c_int