Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the class name and bytecode
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName(), data.getMutatedClass().getBytes());
    // Get the ClassInfo using the ClassInfoBuilder
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData using the ClassInfo
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
Explanation:

The error is caused by the removal of the `getClassInfo()` method from the `CoverageDatabase` class. To fix this, we create a new `ClassInfoBuilder` with the class name and bytecode, and then use its `build()` method to get a `ClassInfo` object. We then pass this `ClassInfo` object to the `MutationTestSummaryData` constructor, along with the other required parameters.


Note that we cannot use the `getClassInfo()` method from the `CoverageDatabase` class, as it has been removed in the new library version. Instead, we use the `ClassInfoBuilder` class to create a new `ClassInfo` object, which can be used in place of the removed method.