Here's a fixed version of the code that uses an added method from the new library version:

```java
import org.tinspin.index.util.MinHeap;

import java.util.Collections;
import java.util.List;

public class FastPolygonizerTests {
    // ...

    @Override
    public void testNoding() {
        List<SegmentString> lines = createLines();
        MinHeap<SegmentString> nodingHeap = new MinHeap<>(lines);
        Collections.sort(lines);

        // ...
    }

    // ...
}
```

In this version, I used the `MinHeap` class that was added in the new version. I changed the import statement to use the new class and updated the type of the `nodingHeap` variable.

Note that since the `MinHeap` class implements the `MinHeapI` interface, the `size()` method is still available for use.