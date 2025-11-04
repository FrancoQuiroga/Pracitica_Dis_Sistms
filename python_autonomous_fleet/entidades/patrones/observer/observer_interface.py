#!/usr/bin/env python3
"""
Modulo que define las interfaces Observer y Observable del patron.
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    La interfaz Observer declara el metodo de actualizacion, usado por
    los Observables (Subjects) para notificar a los observadores.
    """
    
    @abstractmethod
    def actualizar(self, evento: dict):
        """Recibe la notificacion del observable."""
        pass

class Observable(ABC):
    """
    La interfaz Observable (Subject) declara los metodos para gestionar
    suscriptores (observers).
    """
    
    @abstractmethod
    def suscribir(self, observer: Observer):
        """Agrega un observador."""
        pass

    @abstractmethod
    def desuscribir(self, observer: Observer):
        """Elimina un observador."""
        pass

    @abstractmethod
    def notificar(self, evento: dict):
        """Notifica a todos los observadores sobre un evento."""
        pass