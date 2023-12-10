#ifndef __AOC_REGISTRY_H__
#define __AOC_REGISTRY_H__

#include <map>
#include "solution.h"

class Registry {
    protected:
        std::map<int, Solution*> solutions;

    public:
        Registry();
        ~Registry();
        Solution* get_solver(int day);
};

#endif
