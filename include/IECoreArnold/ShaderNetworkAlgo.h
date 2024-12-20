//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2016, Image Engine Design Inc. All rights reserved.
//
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//
//      * Redistributions of source code must retain the above
//        copyright notice, this list of conditions and the following
//        disclaimer.
//
//      * Redistributions in binary form must reproduce the above
//        copyright notice, this list of conditions and the following
//        disclaimer in the documentation and/or other materials provided with
//        the distribution.
//
//      * Neither the name of John Haddon nor the names of
//        any other contributors to this software may be used to endorse or
//        promote products derived from this software without specific prior
//        written permission.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////

#pragma once

#include "IECoreArnold/Export.h"

#include "IECoreScene/ShaderNetwork.h"

#include "IECore/CompoundObject.h"

#include "ai_nodes.h"

#include <vector>

namespace IECoreArnold
{

namespace ShaderNetworkAlgo
{

/// Some Arnold shaders (`camera_projection` particularly) have unhelpful `NODE *`
/// parameters that can't be exposed to users as-is. For these we allow a string
/// parameter value to specify the _name_ of a node, and connect to the node
/// itself at a later date (since the node might not exist when the shader is
/// converted, or might be deleted later).
struct NodeParameter
{
	NodeParameter( AtNode *node, AtString parameterName, AtString parameterValue );
	NodeParameter( const NodeParameter &other ) = default;

	/// Uses `AiNodeLookUpByName()` to find the right node, and assign it to the
	/// parameter.
	void updateParameter() const;

	private :
		AtNode *m_node;
		AtString m_parameterName;
		AtString m_parameterValue;
};

/// Returns a network of `AtNodes` generated by converting `shaderNetwork` to
/// Arnold. The output shader is the last node in the returned vector, and is
/// given the specified `name`. All other nodes will be named uniquely using
/// `name` as a prefix. If provided, `nodeParameters` is filled for later
/// resolution.
IECOREARNOLD_API std::vector<AtNode *> convert( const IECoreScene::ShaderNetwork *shaderNetwork, AtUniverse *universe, const std::string &name, std::vector<NodeParameter> &nodeParameters, const AtNode *parentNode = nullptr );
/// \deprecated
IECOREARNOLD_API std::vector<AtNode *> convert( const IECoreScene::ShaderNetwork *shaderNetwork, AtUniverse *universe, const std::string &name, const AtNode *parentNode = nullptr );
/// Updates a previously converted set of nodes to reflect changes in `shaderNetwork`,
/// reusing AtNodes where possible. The `nodes` vector is updated in place, newly created
/// nodes use the same parent as the original nodes, and unused nodes are destroyed with
/// `AiNodeDestroy`. Returns true if the output shader node is reused.
IECOREARNOLD_API bool update( std::vector<AtNode *> &nodes, std::vector<NodeParameter> &nodeParameters, const IECoreScene::ShaderNetwork *shaderNetwork );
/// \deprecated
IECOREARNOLD_API bool update( std::vector<AtNode *> &nodes, const IECoreScene::ShaderNetwork *shaderNetwork );

/// Converts any UsdPreviewSurface shaders and UsdLuxLights into native Arnold shaders. This conversion
/// is performed automatically by `convert()` and `update()` and is mainly just exposed for the unit
/// tests.
IECOREARNOLD_API void convertUSDShaders( IECoreScene::ShaderNetwork *shaderNetwork );

/// A function that performs substitutions on a shader network, given the full
/// inherited `attributes` for an object. Must be threadsafe.
using SubstitutionFunction = void (*)( IECoreScene::ShaderNetwork *shaderNetwork, const IECore::CompoundObject *attributes );
/// A function that appends to `hash` to uniquely identify the work that will be
/// performed by a SubstitutionFunction. Particular attention must be paid to
/// the performance of any such function, as it will be called frequently. If a
/// substitution will be a no-op, then nothing should be appended to the hash.
/// Must be threadsafe.
using SubstitutionHashFunction = void (*)( const IECoreScene::ShaderNetwork *shaderNetwork, const IECore::CompoundObject *attributes, IECore::MurmurHash &hash );

/// Registers a just-in-time substitution to be performed on shader
/// networks before the shader is translated to Arnold.
IECOREARNOLD_API void registerSubstitution( const std::string &name, SubstitutionHashFunction hashFunction, SubstitutionFunction substitutionFunction );
/// Removes a previously registered substitution with the specified name.
IECOREARNOLD_API void deregisterSubstitution( const std::string &name );

/// Hashes all the currently registered substitutions for `shaderNetwork`.
IECOREARNOLD_API void hashSubstitutions( const IECoreScene::ShaderNetwork *shaderNetwork, const IECore::CompoundObject *attributes, IECore::MurmurHash &hash );
/// Applies all the currently registered substitutions to `shaderNetwork`.
IECOREARNOLD_API void applySubstitutions( IECoreScene::ShaderNetwork *shaderNetwork, const IECore::CompoundObject *attributes );

} // namespace ShaderNetworkAlgo

} // namespace IECoreArnold
