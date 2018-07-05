
#ifndef URL2MSGID_H
#define URL2MSGID_H

#include <vector>
#include <string>


class Url2Msgid {
public:
   
	static std::string encode(const char* url);
	
	static std::string decode(const char* msgid);
	
	
};



#endif