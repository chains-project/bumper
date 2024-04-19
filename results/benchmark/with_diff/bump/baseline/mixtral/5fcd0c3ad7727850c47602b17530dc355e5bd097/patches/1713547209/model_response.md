Here's the proposed patch for the given client code:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;

private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytes = coverage.getClassBytes(className);
    long timestamp = coverage.getTimestamp(className);
    ClassInfo classInfo = ClassInfoBuilder.forClass(className)
        .addClassFileLocation(classBytes)
        .setLastModified(timestamp)
        .build();
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch replaces the usage of the removed `getClassInfo` method with a new `ClassInfo` creation using the added `ClassInfoBuilder`. The `getClassBytes` and `getTimestamp` methods are used to provide the required data for the `ClassInfoBuilder`.