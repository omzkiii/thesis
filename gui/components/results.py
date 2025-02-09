from tkinter import Tk, Label, Button

def display_results(results):
    root = Tk()
    root.title("Runtime Analysis Results")

    Label(root, text=f"Dataset size: {results['samples']} runs").pack()
    Label(root, text=f"Avg ODTC Time: {results['mean_odtc']:.2f} sec").pack()
    Label(root, text=f"Avg TC Time: {results['mean_tc']:.2f} sec").pack()
    Label(root, text=f"Test Used: {results['test_used']}").pack()
    Label(root, text=f"P-value: {results['p_value']:.4f}").pack()

    if results['p_value'] < 0.05:
        Label(root, text="Significant Difference Found (p < 0.05)", fg="red").pack()
    else:
        Label(root, text="No Significant Difference Found", fg="green").pack()

    Button(root, text="Close", command=root.quit).pack()

    root.mainloop()
