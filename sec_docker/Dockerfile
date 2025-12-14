FROM nginx
WORKDIR /app
COPY package*.json ./
COPY . .
RUN useradd -m appuser
USER appuser
CMD ["bash"]

