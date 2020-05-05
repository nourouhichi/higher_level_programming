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
	int i, x = 0, y = 0;
	listint_t *run = *head, *road_runner = *head, *before = NULL, *after;
	int *array;

	if (!*head)
		return (1);
	for (i = 0; road_runner != NULL;)
	{
		i++;
		road_runner = road_runner->next; }
	if (i % 2 != 0)
		return (0);
	array = malloc(sizeof(int) * 10);
	if (!array)
		return (0);
	x = 0;
	array[0] = (*head)->n;
	run = (*head)->next;
	while (run)
	{
		x++;
		array[x] = run->n;
		run = run->next; }
	while (*head)
	{
		after = (*head)->next;
		(*head)->next = before;
		before = *head;
		*head = after; }
	*head = before;
	while (*head)
	{
		if (array[y] != (*head)->n)
		{
			free(array);
			return (0); }
		*head = (*head)->next;
		y++; }
	free(array);
	return (1);
}

