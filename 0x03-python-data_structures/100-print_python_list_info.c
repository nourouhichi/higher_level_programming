#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, j = 0;
	PyObject *list;

	i = (((PyVarObject*)(p))->ob_size);
	printf("[*] Size of the Python List = %lu\n", i);
	printf("[*] Allocated = %lu\n", (((PyListObject *)(p))->allocated));
	while (j < i)
	{
		list = (((PyListObject *)(p))->ob_item[j]);
		printf("Element %lu: %s\n", j, (char *)list->ob_type->tp_name);
		j++;
	}
}
