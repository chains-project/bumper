Here's the proposed patch for the failing method:

```java
import org.pitest.classinfo.ClassInfo;
import org.pitest.classinfo.ClassInfoBuilder;
import org.pitest.classinfo.ClassName;
import org.pitest.coverage.CoverageDatabase;

private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] classBytecode = // fetch the bytecode for the mutated class
    long timestamp = // fetch the timestamp for the mutated class

    ClassInfo classInfo = ClassInfoVisitor.getClassInfo(className, classBytecode, timestamp);

    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```

This patch introduces a couple of new variables to hold the bytecode and timestamp of the mutated class. It then uses the new `getClassInfo` method from `ClassInfoVisitor` to create a `ClassInfo` instance using the provided class information.

Please note that you need to replace the `// fetch the bytecode for the mutated class` and `// fetch the timestamp for the mutated class` comments with actual code to fetch the required information. This information can be obtained from the `coverage` object or any other relevant source.