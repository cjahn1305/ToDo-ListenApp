// Ticket 1: Ladeanimation und verzögerte Anzeige der Login-Seite
import React, { useEffect, useState } from "react";

function Loading() {
  return <div>Loading...</div>;
}

function LoginPage() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setLoading(false);
    }, 3000);
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return <Loading />;
  }

  // Ticket 4: Login-Komponente
  return (
    <div>
      <h2>Login</h2>
      <form>
        <input type="text" placeholder="Benutzername" />
        <input type="password" placeholder="Passwort" />
        <label>
          <input type="checkbox" />
          Eingeloggt bleiben
        </label>
        <button type="submit">Anmelden</button>
      </form>
    </div>
  );
}

export default LoginPage;
