#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a node at a known index
 * @head: pointer to the head of the list
 * @number:number to be compared
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *road_runner, *new;
	int idx = 0, i = 0;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	road_runner = *head;
	if (!road_runner)
	{
		*head = new;
		new->next = NULL;
		return (new); }
	while ((road_runner) && (road_runner->n < number))
	{
		road_runner = road_runner->next;
		idx++; }
	if (idx == 0)
	{
		new->next = *head;
		*head = new;
		return (new); }
	road_runner = *head;
	while ((road_runner) && (i != (idx - 1)))
	{
		road_runner = road_runner->next;
		i++;
		if (!road_runner)
		{
			free(new);
			return (NULL); }
	}
	new->next = road_runner->next;
	road_runner->next = new;
	return (new); }

