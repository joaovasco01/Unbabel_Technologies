package main

import (
	"fmt"
	"os" // Import to use command line arguments

	"github.com/cdipaolo/sentiment"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: sentiment_analysis <text>")
		os.Exit(1)
	}
	text := os.Args[1] // Get text from the first command line argument
	score := AnalyzeSentiment(text)
	fmt.Printf("Sentiment score for '%s': %d\n", text, score)
}

// AnalyzeSentiment returns the sentiment score for the given text
func AnalyzeSentiment(text string) int {
	model, err := sentiment.Restore()
	if err != nil {
		panic(err)
	}

	analysis := model.SentimentAnalysis(text, sentiment.English)
	return int(analysis.Score)
}
