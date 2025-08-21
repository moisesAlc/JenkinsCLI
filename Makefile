# Nome do ambiente virtual
VENV = venv

# Alvo padrão
.PHONY: run

# Cria venv e instala dependências
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

# Roda o script para exportar builds
run: $(VENV)/bin/activate
	$(VENV)/bin/python jenkins_history_csv.py

