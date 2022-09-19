class A {
    int roll, marks;
    String name;

    A(int roll, String name, int marks) {
        this.roll = roll;
        this.name = name;
        this.marks = marks;
    }

    void display() {
        System.out.println("Roll: " + roll);
        System.out.println("Name: " + name);
        System.out.println("Marks: " + marks);
    }
}

class B extends A {
    int total;

    B(int roll, String name, int marks, int total) {
        super(roll, name, marks);
        this.total = total;
    }

    void display() {
        super.display();
        System.out.println("Total: " + total);
    }

    public static void main(String[] args) {
        B obj = new B(1, "John", 90, 100);
        obj.display();
    }

}
