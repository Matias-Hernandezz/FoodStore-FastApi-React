import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AdminLayout } from "./components/AdminLayout";
import { CategoriasPage } from "./pages/admin/CategoriasPage";
import { ProductosPage } from "./pages/admin/ProductosPage";
import { IngredientesPage } from "./pages/admin/IngredientesPage";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 30, // 30 segundos
      retry: 1,
    },
  },
});

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate to="/admin/categorias" replace />} />
          <Route
            path="/admin/*"
            element={
              <AdminLayout>
                <Routes>
                  <Route path="categorias" element={<CategoriasPage />} />
                  <Route path="productos" element={<ProductosPage />} />
                  <Route path="ingredientes" element={<IngredientesPage />} />
                  <Route path="*" element={<Navigate to="categorias" replace />} />
                </Routes>
              </AdminLayout>
            }
          />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}
