select
	*
from teacher
where tid
= (select
	teacher_id
from course);
