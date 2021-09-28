# Coding Task

Implement a system where we can have a Teacher and Student.
One teacher can have many students, and students can have many teachers.

Should be able to do the following:

- List/add/edit/delete teachers.
- List/add/edit/delete students.
- Even though teachers teach all their associated students, they would like to highlight exceptional students with a “star”. So please implement this capability to start one or more students that they teach.

> Please implement using Django ORM, templates, forms, etc.

Extra credit/feature: Implement a GraphQL endpoint with a query for teachers and a query for students. An example query it should support is “list of teachers and all the students they have starred”. In addition, please implement a mutation that enables the starring (or removing of the star) of a student associated with a teacher.

## Goals

- Setup codebase from scratch with whatever structure you’d like and is best practice.
- Deliver a Github public link; instead of a single big “first commit” try to push code commit by commit so Git history represents how the codebase has been evolving over time.
- The codebase should be dockerized meaning ‘docker-compose up’ should just work once we clone the codebase.
- Make your code as well documented and cleanly structured as possible. Please include a README.md file with instructions/thoughts (if any)
- Please add a couple of unit tests as well as appropriate. Include code coverage numbers/details in the README or your response.
- Feel free to use bootstrap, material design, or similar libraries to implement.
- Please use your best judgment for any open questions.
