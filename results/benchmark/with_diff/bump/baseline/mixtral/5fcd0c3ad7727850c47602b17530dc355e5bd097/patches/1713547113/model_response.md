Here's the proposed patch for the given client code:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.CoverageDatabase;
import org.pitest.mutationtest.MutationTestListener;
import org.pitest.mutationtest.engine.gregor.MutationResult;

private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final MutationTestListener.MutationResult data) {
    ClassName className = data.getMutatedClass();
    byte[] classfile = coverage.getClassfile(className);
    long timestamp = coverage.getTimestamp(className);
    ClassInfo classInfo = ClassInfoBuilder.forClass(className, classfile, timestamp)
            .build();
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

In the patched code, I replaced the `getClassInfo` method from the `CoverageDatabase` with the new method `getClassfile` and `getTimestamp` to get the classfile and timestamp respectively. Then, I used the `ClassInfoBuilder` to build the `ClassInfo` object using the classname, classfile, and timestamp.