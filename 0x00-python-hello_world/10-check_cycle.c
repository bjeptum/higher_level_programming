#include "lists.h"
#include<stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @slow: slow pointer
 * @fast: fast pointer
 *
 * Return: 1 else 0
 */
int check_cycle(listint_t *list);
{
    listint_t *slow = list;
    listint *fast = list;
    
    while(slow && fast && fast->next)
    {
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
	{
	    return (1);
	}
    }
    return (0);
}
