#include "lists.h"
#include "stdio.h"
/**
 *check_cycle - checks if the linked list has a cycle in it
 *@list: the linked list to be checked
 *Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *roadrunner;

	if (!list)
		return(0);
	first = list;
	roadrunner = list->next;
	do
	{
		while (roadrunner)
		{
			if (roadrunner == first)
				return (1);
			roadrunner = roadrunner->next;

		}
		first = first->next;
	}while (first);
	return (0);
}

