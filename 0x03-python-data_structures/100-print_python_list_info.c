#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
  * print_python_list_info - Prinnts basic info of Python list
  * @p: Python object in this case a list
  * Return: Size, memory and type of list element
**/
void print_python_list_info(PyObject *p)
{
	/*Find the size of the list using PyList_Size*/
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Size of the Python List = %zd\n", size);

    /*Amount of memory allocated for the list*/
    PyListObject *list = (PyListObject *) p;
    Py_ssize_t allocated = list->allocated;
    printf("[*] Allocated Memory = %zd\n", allocated);

    /*Loop through each element in the list and print type*/
    printf("[*] Element types:\n");
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(p, i);
        const char *type_name = element->ob_type->tp_name;
        printf("Element [%zd]: %s\n", i, type_name);
    }
}
