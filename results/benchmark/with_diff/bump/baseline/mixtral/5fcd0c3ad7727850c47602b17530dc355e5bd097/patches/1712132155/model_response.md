Based on the error message and the library changes, it seems that the `getClassInfo` method of `CoverageDatabase` is no longer available in the new library version. Instead, there is a new `getClassInfo` static method in `ClassInfoBuilder` that can be used to create `ClassInfo` objects. Here's a possible patch for the failing method:
```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classfile = coverage.getClassfile(mutatedClass);
    long timestamp = coverage.getTimestamp(mutatedClass);
    ClassInfo classInfo = ClassInfoBuilder.getClassInfo(mutatedClass, classfile, timestamp);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
This patch creates a `ClassInfo` object using the new `getClassInfo` method in `ClassInfoBuilder`, passing the mutated class name, classfile, and timestamp as arguments. The rest of the method remains unchanged.