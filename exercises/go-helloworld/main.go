package main

import (
	"fmt"
	"log"
	"net/http"
)

func helloWorld(w http.ResponseWriter, r *http.Request) {
	log.Println("Received", r.Method, "at", r.URL)
	lines, err := fmt.Fprintf(w, "Hello World")
	if err != nil {
		log.Println(err)
		return
	}
	log.Println("Written", lines, "lines")
}

func main() {
	http.HandleFunc("/", helloWorld)
	err := http.ListenAndServe(":6111", nil)
	if err != nil {
		return
	}
}
