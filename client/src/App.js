import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import Preferences from "./components/Preferences";
import Login from "./components/Login";
import useToken from "./api/useToken";

function App() {
  const { token, setToken } = useToken();

  if (!token) {
    return <Login setToken={setToken} />;
  }

  return (
    <div
      style={{
        background: "#231a0f",
      }}
    >
      <div className="flex items-center justify-between w-10/12 mx-auto py-3 text-white">
        <h1 className="text-3xl font-bold">
          Students API
          <span className="w-3 h-3 bg-red-500 inline-block rounded-full"></span>
        </h1>
        <BrowserRouter>
          <Switch>
            <Route path="/">
              <Dashboard />
            </Route>
            <Route path="/preferences">
              <Preferences />
            </Route>
          </Switch>
        </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
