# AI Ticket System - OOP Learning Project

## Overview

The **AI Ticket System** is a Python-based Help Desk application developed to learn **Object-Oriented Programming (OOP)** from the ground up. Although the project simulates a real-world ticket management system, its primary objective is to understand OOP concepts, software design principles, and how multiple classes collaborate to solve a business problem.

The system manages users, creates support tickets, assigns tickets to the appropriate teams, tracks ticket status and priority, validates user inputs, and manages multiple tickets through a central manager class.

---

# System Architecture

```
                User
                  │
                  ▼
           Creates Ticket
                  │
                  ▼
      Technical / Payment / Account
             Ticket Objects
                  │
                  ▼
           assign_team()
                  │
                  ▼
           TicketManager
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
Update Status         Update Priority
      │                       │
      └───────────┬───────────┘
                  ▼
         Display Ticket Summary
```

---

# Project Structure

```
ai_ticket_system/

├── main.py
├── ticket.py
├── user.py
├── ticket_manager.py
├── constants.py
└── exceptions.py
```

---

# Components

## User

Represents a customer or employee who creates support tickets.

### Responsibilities

* Store user information
* Update user details
* Display user information

---

## Ticket (Abstract Base Class)

Acts as the common blueprint for every support ticket.

### Responsibilities

* Store ticket details
* Validate status and priority
* Update ticket information
* Display ticket summary
* Define the abstract `assign_team()` contract

---

## TechnicalTicket

Represents technical issues.

Assigns tickets to the **Technical Team**.

---

## PaymentTicket

Represents payment-related issues.

Assigns tickets to the **Finance Team**.

---

## AccountTicket

Represents account-related issues.

Assigns tickets to the **Support Team**.

---

## TicketManager

Acts as the controller of the application.

### Responsibilities

* Add tickets
* Remove tickets
* Search tickets
* Update ticket status
* Update ticket priority
* Display all tickets

---

## Constants

Stores reusable application-wide values.

Examples:

* Priorities
* Ticket Statuses

---

## Exceptions

Contains custom exception classes.

Examples:

* InvalidPriorityError
* InvalidStatusError

---

# OOP Concepts Learned

## Phase 1: OOP Basics ✅

* Class
* Object
* Attributes
* Methods
* `self`
* Constructor (`__init__`)
* Object State
* Object Behavior

---

## Phase 2: Composition ✅

* Multiple classes working together
* `TicketManager` contains multiple `Ticket` objects
* Has-a relationship

---

## Phase 3: Encapsulation ✅

* Private attributes
* Getters
* Validation methods
* Controlled updates
* Information hiding
* Custom exceptions

---

## Phase 4: Inheritance ✅

```
Ticket
│
├── TechnicalTicket
├── PaymentTicket
└── AccountTicket
```

* Parent class
* Child classes
* Constructor inheritance

---

## Phase 5: Polymorphism ✅

Same method call.

Different implementation.

```
ticket.assign_team()
```

Each ticket type performs its own behavior.

---

## Phase 6: Method Overriding ✅

Each child class overrides:

```
assign_team()
```

Examples:

* TechnicalTicket → Technical Team
* PaymentTicket → Finance Team
* AccountTicket → Support Team

---

## Phase 7: `super()` ✅

Reuse parent constructors and methods without duplicating code.

---

## Phase 8: `isinstance()` ✅

Determine whether an object belongs to a class or any of its parent classes.

---

## Phase 9: Method Resolution Order (MRO) ✅

Understand how Python searches for methods in an inheritance hierarchy.

```
TechnicalTicket
        ↓
Ticket
        ↓
object
```

---

## Phase 10: Abstract Base Classes (ABC) ✅

The `Ticket` class defines a common contract.

Every child class must implement:

```
assign_team()
```

This prevents incomplete implementations and enforces consistency.

---

# Software Design Principles

* Object-Oriented Programming
* Separation of Concerns
* DRY (Don't Repeat Yourself)
* Code Reusability
* Data Validation
* Information Hiding
* Modular Design
* Composition
* Inheritance
* Polymorphism

---

# OOP Learning Roadmap

| Phase                           | Status |
| ------------------------------- | ------ |
| Phase 1: OOP Basics             | ✅      |
| Phase 2: Composition            | ✅      |
| Phase 3: Encapsulation          | ✅      |
| Phase 4: Inheritance            | ✅      |
| Phase 5: Polymorphism           | ✅      |
| Phase 6: Method Overriding      | ✅      |
| Phase 7: `super()`              | ✅      |
| Phase 8: `isinstance()`         | ✅      |
| Phase 9: MRO                    | ✅      |
| Phase 10: Abstract Base Classes | ✅      |

---

# Future Enhancements

* [ ] Class Variables
* [ ] Static Methods
* [ ] Class Methods
* [ ] Magic Methods (`__str__`, `__repr__`, `__eq__`, etc.)
* [ ] File Persistence (JSON / CSV)
* [ ] Unit Testing (`unittest` / `pytest`)
* [ ] SOLID Principles
* [ ] Logging
* [ ] Database Integration
* [ ] REST API using Flask or FastAPI

---

# Learning Outcomes

By completing this project, I gained hands-on experience with:

* Designing object-oriented systems
* Building modular and reusable code
* Applying the four pillars of OOP
* Working with inheritance hierarchies
* Implementing abstraction using abstract base classes
* Using composition to manage object relationships
* Applying encapsulation through private attributes and validation
* Handling errors with custom exceptions
* Understanding polymorphism, method overriding, `super()`, `isinstance()`, and MRO

This project serves as a strong foundation for building larger Python applications and demonstrates the practical application of Object-Oriented Programming concepts used in real-world software systems.
