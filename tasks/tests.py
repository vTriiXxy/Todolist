from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            titulo="Tarea de prueba",
            descripcion="Descripción de prueba",
            estado="pendiente"
        )
        self.assertEqual(str(task), "Tarea de prueba")
        self.assertEqual(task.get_estado_display(), "Pendiente")
        self.assertIsNotNone(task.fecha_creacion)

class TaskViewsTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            titulo="Tarea inicial",
            descripcion="Descripción inicial",
            estado="pendiente"
        )

    def test_task_list_get(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarea inicial")

    def test_task_create_post(self):
        response = self.client.post(reverse('task_list'), {
            'titulo': 'Nueva tarea creada',
            'descripcion': 'Contenido',
            'estado': 'en_progreso'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(titulo='Nueva tarea creada').exists())

    def test_task_detail(self):
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarea inicial")

    def test_task_update(self):
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'titulo': 'Tarea editada',
            'descripcion': 'Descripción actualizada',
            'estado': 'completada'
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.titulo, 'Tarea editada')
        self.assertEqual(self.task.estado, 'completada')

    def test_task_delete(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
