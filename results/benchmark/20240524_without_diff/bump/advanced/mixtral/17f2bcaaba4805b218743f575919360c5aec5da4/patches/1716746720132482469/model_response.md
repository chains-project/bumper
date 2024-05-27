Here's the fixed version of the client code that removes the failing static import statement:

```java
import org.junit.Test;
import org.junit.AssumptionViolatedException;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testSomething() {
        assumeTrue(someCondition());
    }

    private boolean someCondition() {
        // ...
        return true; // or false, depending on the condition
    }
}
```

Instead of using the static import, we can create a helper method `assumeTrue` that throws an `AssumptionViolatedException` if the assumption is not met:

```java
import org.junit.Test;
import org.junit.AssumptionViolatedException;

public class PGS_MorphologyGroupShapeTests {

    @Test
    public void testSomething() {
        assumeTrue(someCondition());
    }

    private boolean someCondition() {
        // ...
        return true; // or false, depending on the condition
    }

    private void assumeTrue(boolean condition) {
        if (!condition) {
            throw new AssumptionViolatedException("Assumption not met");
        }
    }
}
```

This way, we achieve the same behavior without using the static import.