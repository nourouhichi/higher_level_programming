#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks is a list is a palin
 * @head: pointer to the head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *runner = *head;
	int x = 0, i, j, array[1024];

	if (!head || !*head || !(*head)->next)
		return (1);
	for (i = 0; runner; i++)
	{
		array[i] = runner->n;
		runner = runner->next; 
	}
	x = i / 2;
	for (i--, j = 0; i <= x ; i--, j++)
	{
		if (array[i] != array[j])
		{
			return (0);
		}
	}
	return (1);
}

