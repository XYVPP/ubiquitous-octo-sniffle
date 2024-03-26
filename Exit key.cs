using UnityEngine;

public class ApplicationManager : MonoBehaviour
{
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            ExitApplication();
        }
    }

    public void ExitApplication()
    {
        Application.Quit();
    }
}