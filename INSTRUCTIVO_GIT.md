# Instructivo para Sincronizar un Repositorio Local con GitHub

Este instructivo detalla los pasos necesarios para crear un repositorio en GitHub y sincronizarlo con un repositorio local, teniendo en cuenta la presencia de un archivo `README.md` en el repositorio remoto.

---

## **Pasos a seguir**

1. **Crear el repositorio en GitHub**
   - Ve a GitHub y crea un nuevo repositorio.
   - Asegúrate de marcar la opción para incluir un archivo `README.md` si deseas inicializar el repositorio con documentación básica.

2. **Crear la carpeta en el equipo local**
   - En tu equipo, crea una carpeta que será tu repositorio local. Por ejemplo:
     ```bash
     mkdir nombre_del_repositorio
     cd nombre_del_repositorio
     ```

3. **Inicializar el repositorio local**
   - Inicializa Git dentro de la carpeta local:
     ```bash
     git init
     ```

4. **Agregar el repositorio remoto**
   - Enlaza tu repositorio local al remoto de GitHub:
     ```bash
     git remote add origin https://github.com/tu_usuario/nombre_del_repositorio.git
     ```

5. **Agregar los archivos locales al repositorio**
   - Si tienes archivos en la carpeta local, agrégalos al área de preparación:
     ```bash
     git add .
     ```

6. **Hacer el primer commit**
   - Guarda los cambios en el repositorio local:
     ```bash
     git commit -m "Primer commit"
     ```

7. **Traer los cambios del repositorio remoto**
   - Si el repositorio remoto en GitHub tiene un archivo `README.md` u otros cambios iniciales, necesitas sincronizarlo con tu repositorio local. Usa el siguiente comando:
     ```bash
     git pull origin main --rebase
     ```
     
   - **Nota:** Si tu rama principal se llama `master` en lugar de `main`, reemplaza `main` por `master`.

8. **Subir los cambios al repositorio remoto**
   - Después de haber sincronizado los cambios, sube tus archivos locales al repositorio remoto:
     ```bash
     git push -u origin main
     ```

---

## **Notas adicionales**

- **Resolución de conflictos:** Si al realizar el `git pull` aparecen conflictos, Git te notificará. Debes resolver los conflictos manualmente en los archivos afectados y luego ejecutar:
  ```bash
  git add .
  git rebase --continue
  ```

- **Forzar un push (opcional):** Si estás seguro de que deseas sobrescribir los cambios remotos con tu versión local, usa el comando:
  ```bash
  git push origin main --force
  ```
  
  **Advertencia:** Esto eliminará cualquier cambio realizado en el repositorio remoto.

- **Verificar la rama principal:** Algunos repositorios utilizan `master` como rama principal en lugar de `main`. Usa `git branch -r` para verificar el nombre de la rama principal remota.

---

Este instructivo asegura que tu repositorio local y remoto estén sincronizados correctamente. Si tienes problemas en algún paso, no dudes en buscar ayuda adicional.

