Here's a proposed patch to fix the failing client code:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the class name and bytecode
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass());
    // Get the class info using the ClassInfoBuilder
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData using the class info
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch creates a new `ClassInfoBuilder` with the mutated class name and bytecode, then uses it to build a `ClassInfo` object. The `ClassInfo` object is then passed to the `MutationTestSummaryData` constructor instead of the `CoverageDatabase` object.

This patch fixes the error by using the new `ClassInfoBuilder` class to get the class info, instead of relying on the removed `getClassInfo` method in the `CoverageDatabase` class.